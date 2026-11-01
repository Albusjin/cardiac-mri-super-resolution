#!/usr/bin/env python3
"""Read the frozen onboarding snapshot; standard library only, no GPU calls."""
import csv
import json
from pathlib import Path


def main():
    package = Path(__file__).resolve().parents[1]
    snapshot = json.loads(
        (package / 'evidence/ixi_training_snapshot.json').read_text(encoding='utf-8')
    )
    print('研究组资料包：冻结快照，不会访问实时训练')
    print('快照时间：', snapshot['snapshot_at'])
    for name, status in snapshot['stages'].items():
        print(
            f"{name}: {status['state']} | "
            f"{status['iteration']:,}/{status['total_iterations']:,} 步 | "
            f"GPU {status['gpu']}"
        )
    latest = snapshot['stages']['stage2']['validation']
    print(
        f"最近 Stage 2 ×4 验证：step {latest['iter']:,}, "
        f"PSNR {latest['psnr']:.3f} dB, SSIM {latest['ssim']:.5f}"
    )
    print('完整原方法训练与最终 TEST 尚未完成。')
    print('\nACDC 独立患者测试（患者等权，数值按报告精度）：')
    with (package / 'evidence/acdc_test_aggregate.csv').open(
        encoding='utf-8', newline=''
    ) as handle:
        for row in csv.DictReader(handle):
            print(
                f"  {row['method']}: {float(row['psnr_db']):.3f} dB / "
                f"SSIM {float(row['ssim']):.5f}"
            )
    print('\n结论：心脏空间微调有效；时序改动暂无稳定实用增益。')


if __name__ == '__main__':
    main()
