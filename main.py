import json
from pathlib import Path

STEPS = [
    ('validate', '验证需求与问题'),
    ('bp', '撰写商业计划'),
    ('policy', '检查政策合规'),
    ('pitch', '准备路演材料'),
    ('growth', '设计获客路径'),
    ('pricing', '制定定价策略'),
    ('register', '完成公司/产品注册'),
]

DATA = Path('startup_progress.json')


def load():
    if DATA.exists():
        return json.loads(DATA.read_text(encoding='utf-8'))
    return {key: False for key, _ in STEPS}


def save(state):
    DATA.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')


def show(state):
    print('\nAI Startup Skills · 7 步进度')
    for i, (key, label) in enumerate(STEPS, 1):
        mark = '✓' if state.get(key) else '○'
        print(f'{i}. [{mark}] {label}')


def next_step(state):
    for key, label in STEPS:
        if not state.get(key):
            return key, label
    return None, '全部完成，可以开始迭代增长！'


def main():
    state = load()
    while True:
        show(state)
        key, label = next_step(state)
        if key is None:
            print(label)
            break
        answer = input(f'\n下一步建议：{label}\n完成了吗？(y/n/q): ').strip().lower()
        if answer == 'q':
            break
        if answer == 'y':
            state[key] = True
            save(state)
            print('已记录进度。')
        elif answer == 'n':
            print('继续准备，完成后再次运行。')
        else:
            print('请输入 y、n 或 q。')


if __name__ == '__main__':
    main()