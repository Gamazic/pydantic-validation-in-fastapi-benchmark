from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def parse_latency_and_rps(file_name):
    with open(file_name, "r") as f:
        content = f.read().split("\n")
    latency_rpc_lines = content[3: 5]
    latency_rpc = [line.split()[1] for line in latency_rpc_lines]
    return {
        "file_name": str(file_name.name),
        "latency": float(latency_rpc[0][:-2]),
        "rpc": float(latency_rpc[1]),
    }

parsed = []

for file_name in Path("results").glob("*"):
    parsed.append(parse_latency_and_rps(file_name))
df = pd.DataFrame(parsed)
df = df.set_index("file_name").sort_values(by="latency")
print(df)
df.plot.barh()
df.to_csv("benchmark_results.csv", sep=",", )
plt.savefig('benchmark_results.png')
plt.show()
