import simpy
import random
import numpy as np
from dataclasses import dataclass

@dataclass
class MedicalDevice:
    dev_id: int         # 设备 ID
    data_size: float    # 总数据量 (MB)
    channel_gain: float # 信道增益 (dB)
    alpha: float = 0.1  # 速率拆分因子 (公共流速率占比)
    p: float = 0.3      # 功率分配比例 (公共流功率占比)

class IoMTSystem:
    def __init__(self, env, num_devices=5, r_max=100, c_max=50):
        self.env = env
        self.num_devices = num_devices
        self.r_max = r_max    # 最大传输速率 (MB/s)
        self.c_max = c_max    # 最大计算速率 (MB/s)
        self.base_station = simpy.Resource(env, capacity=1)  # 基站接收资源
        self.edge_server = simpy.Resource(env, capacity=2)  # 边缘服务器计算资源

    def data_offload(self, device: MedicalDevice):
        """数据卸载阶段：拆分信号并传输"""
        # 信号拆分
        device.d_c = device.data_size * random.uniform(0.1, 0.3)  # 公共流数据量 (10 - 30%)
        device.d_p = device.data_size - device.d_c
        # 传输速率计算
        r_c = device.alpha * self.r_max  # 公共流速率
        r_p = (1 - device.alpha) * self.r_max  # 私有流速率
        # 传输时延（含功率分配影响）
        t_c = device.d_c / (r_c * device.p)  # 公共流传输时间
        t_p = device.d_p / (r_p * (1 - device.p))  # 私有流传输时间
        yield self.env.timeout(t_c + t_p)
        print(f"设备{device.dev_id}完成卸载，总传输时延：{t_c + t_p:.2f}s")

    def parallel_processing(self, device: MedicalDevice):
        """并行处理阶段：边缘服务器计算"""
        # 计算资源分配（公共/私有流并行处理）
        c_c = random.uniform(10, self.c_max)  # 公共流计算速率
        c_p = random.uniform(10, self.c_max)  # 私有流计算速率
        t_c_process = device.d_c / c_c
        t_p_process = device.d_p / c_p
        process_time = max(t_c_process, t_p_process)  # 均衡处理时间
        with self.edge_server.request() as req:
            yield req
            yield self.env.timeout(process_time)
        print(f"设备{device.dev_id}完成处理，处理时延：{process_time:.2f}s")

    def result_feedback(self, device: MedicalDevice):
        """结果反馈阶段：下行传输"""
        feedback_data = device.data_size * 0.1  # 反馈数据量（原始数据 10%）
        t_feedback = feedback_data / (self.r_max * 0.8)  # 下行速率假设为 80MB/s
        yield self.env.timeout(t_feedback)
        print(f"设备{device.dev_id}完成反馈，反馈时延：{t_feedback:.2f}s")

    def run_simulation(self):
        """全流程仿真"""
        devices = [MedicalDevice(
            dev_id=i,
            data_size=random.uniform(50, 100),  # 数据量 50 - 100MB
            channel_gain=random.uniform(-10, 0)  # 信道增益 -10 ~ 0dB
        ) for i in range(self.num_devices)]

        # 按信道增益降序排序（SIC 解码顺序）
        devices.sort(key=lambda x: x.channel_gain, reverse=True)

        for device in devices:
            print(f"\n---- 设备{device.dev_id}开始处理 ----")
            yield self.env.process(self.data_offload(device))
            yield self.env.process(self.parallel_processing(device))
            yield self.env.process(self.result_feedback(device))

# 仿真执行
if __name__ == "__main__":
    env = simpy.Environment()
    system = IoMTSystem(env, num_devices=3)
    env.process(system.run_simulation())
    env.run()
    