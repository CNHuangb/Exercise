import numpy as np
import pandas as pd

# 设置随机种子以确保结果可重现
np.random.seed(42)

# 定义组别大小
n_obs = 43  # 观察组人数
n_con = 42  # 对照组人数
total_n = n_obs + n_con

# 创建空的数据框架
columns = [
    'ID', '组别', 
    '护理前肿胀直径', '护理7天肿胀直径', 
    '护理前硬结直径', '护理7天硬结直径', 
    '护理前瘀斑直径', '护理7天瘀斑直径',
    '肿胀消退时间', '瘀斑吸收时间', '局部皮温',
    '感染', '血肿', '皮肤瘙痒', '满意'
]

df = pd.DataFrame(columns=columns)

# 生成ID
df['ID'] = range(1, total_n+1)
df['组别'] = ['观察组'] * n_obs + ['对照组'] * n_con

# 1. 生成肿胀数据
# 观察组: 3人有肿胀，40人无肿胀
swelling_obs = np.zeros(n_obs)
swelling_obs_idx = np.random.choice(n_obs, 3, replace=False)
swelling_obs[swelling_obs_idx] = np.random.normal(3.45, 0.62, 3)

# 对照组: 2人有肿胀，40人无肿胀
swelling_con = np.zeros(n_con)
swelling_con_idx = np.random.choice(n_con, 2, replace=False)
swelling_con[swelling_con_idx] = np.random.normal(3.42, 0.65, 2)

df['护理前肿胀直径'] = np.concatenate([swelling_obs, swelling_con])

# 2. 生成硬结数据
# 观察组: 20人有硬结，23人无硬结
induration_obs = np.zeros(n_obs)
induration_obs_idx = np.random.choice(n_obs, 20, replace=False)
induration_obs[induration_obs_idx] = np.random.normal(4.33, 1.37, 20)

# 对照组: 20人有硬结，22人无硬结
induration_con = np.zeros(n_con)
induration_con_idx = np.random.choice(n_con, 20, replace=False)
induration_con[induration_con_idx] = np.random.normal(4.15, 1.40, 20)

df['护理前硬结直径'] = np.concatenate([induration_obs, induration_con])

# 3. 生成瘀斑数据
# 观察组: 20人有瘀斑，23人无瘀斑
ecchymosis_obs = np.zeros(n_obs)
ecchymosis_obs_idx = np.random.choice(n_obs, 20, replace=False)
ecchymosis_obs[ecchymosis_obs_idx] = np.random.normal(5.36, 1.40, 20)

# 对照组: 20人有瘀斑，22人无瘀斑
ecchymosis_con = np.zeros(n_con)
ecchymosis_con_idx = np.random.choice(n_con, 20, replace=False)
ecchymosis_con[ecchymosis_con_idx] = np.random.normal(5.12, 1.57, 20)

df['护理前瘀斑直径'] = np.concatenate([ecchymosis_obs, ecchymosis_con])

# 4. 生成护理7天后的数据
# 肿胀 - 观察组
df.loc[df['组别'] == '观察组', '护理7天肿胀直径'] = np.where(
    df.loc[df['组别'] == '观察组', '护理前肿胀直径'] > 0,
    np.random.normal(0.71, 0.15, n_obs),
    0
)

# 肿胀 - 对照组
df.loc[df['组别'] == '对照组', '护理7天肿胀直径'] = np.where(
    df.loc[df['组别'] == '对照组', '护理前肿胀直径'] > 0,
    np.random.normal(1.24, 0.22, n_con),
    0
)

# 硬结 - 观察组
df.loc[df['组别'] == '观察组', '护理7天硬结直径'] = np.where(
    df.loc[df['组别'] == '观察组', '护理前硬结直径'] > 0,
    np.random.normal(0.68, 0.13, n_obs),
    0
)

# 硬结 - 对照组
df.loc[df['组别'] == '对照组', '护理7天硬结直径'] = np.where(
    df.loc[df['组别'] == '对照组', '护理前硬结直径'] > 0,
    np.random.normal(2.29, 0.24, n_con),
    0
)

# 瘀斑 - 观察组
df.loc[df['组别'] == '观察组', '护理7天瘀斑直径'] = np.where(
    df.loc[df['组别'] == '观察组', '护理前瘀斑直径'] > 0,
    np.random.normal(0.65, 0.12, n_obs),
    0
)

# 瘀斑 - 对照组
df.loc[df['组别'] == '对照组', '护理7天瘀斑直径'] = np.where(
    df.loc[df['组别'] == '对照组', '护理前瘀斑直径'] > 0,
    np.random.normal(1.79, 0.21, n_con),
    0
)

# 5. 生成表3的数据
df.loc[df['组别'] == '观察组', '肿胀消退时间'] = np.random.normal(4.20, 1.10, n_obs)
df.loc[df['组别'] == '对照组', '肿胀消退时间'] = np.random.normal(6.50, 1.30, n_con)

df.loc[df['组别'] == '观察组', '瘀斑吸收时间'] = np.random.normal(5.80, 1.20, n_obs)
df.loc[df['组别'] == '对照组', '瘀斑吸收时间'] = np.random.normal(8.10, 1.50, n_con)

df.loc[df['组别'] == '观察组', '局部皮温'] = np.random.normal(36.12, 0.45, n_obs)
df.loc[df['组别'] == '对照组', '局部皮温'] = np.random.normal(36.98, 0.62, n_con)

# 6. 生成表4的数据 (并发症和满意度)
# 观察组: 2例皮肤瘙痒
df.loc[df['组别'] == '观察组', '皮肤瘙痒'] = 0
obs_itching_idx = np.random.choice(df[df['组别'] == '观察组'].index, 2, replace=False)
df.loc[obs_itching_idx, '皮肤瘙痒'] = 1

# 对照组: 1例感染
df.loc[df['组别'] == '对照组', '感染'] = 0
con_infection_idx = np.random.choice(df[df['组别'] == '对照组'].index, 1, replace=False)
df.loc[con_infection_idx, '感染'] = 1

# 所有患者无血肿
df['血肿'] = 0

# 观察组: 40人满意 (93.02%)
df.loc[df['组别'] == '观察组', '满意'] = 0
obs_satisfied_idx = np.random.choice(df[df['组别'] == '观察组'].index, 40, replace=False)
df.loc[obs_satisfied_idx, '满意'] = 1

# 对照组: 32人满意 (76.19%)
df.loc[df['组别'] == '对照组', '满意'] = 0
con_satisfied_idx = np.random.choice(df[df['组别'] == '对照组'].index, 32, replace=False)
df.loc[con_satisfied_idx, '满意'] = 1

# 确保所有值都是非负的
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].clip(lower=0)

# 保存为CSV文件
df.to_csv('85例患者完整数据.csv', index=False, encoding='utf-8-sig')

print("85例患者的完整数据已生成并保存为 '85例患者完整数据.csv'")
print("前10行数据预览:")
print(df.head(10))