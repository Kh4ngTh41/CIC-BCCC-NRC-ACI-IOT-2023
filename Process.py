import pandas as pd
import numpy as np

df_benign = pd.read_csv('Benign Traffic.csv')
df_bf = pd.read_csv('Dictionary Brute Force.csv')
df_DoS_dns_flood = pd.read_csv('DoS DNS Flood.csv')
df_DoS_ICMP = pd.read_csv('DoS ICMP Flood.csv')
df_DoS_SYN = pd.read_csv('DoS SYN Flood.csv')
df_DoS_UDP = pd.read_csv('DoS UDP Flood.csv')
df_mitm = pd.read_csv('MITM ARP Spoofing.csv')
df_recon_HostDiscovery = pd.read_csv('Recon Host Discovery.csv')
df_recon_OS = pd.read_csv('Recon OS Scan.csv')
df_recon_pingsweep = pd.read_csv('Recon Ping Sweep.csv')
df_recon_portscan = pd.read_csv('Recon Port Scan.csv')
df_recon_vul_scan = pd.read_csv('Recon Vulnerability Scan.csv')
df_all = pd.concat([
    df_benign, df_bf, df_DoS_dns_flood, df_DoS_ICMP, df_DoS_SYN, df_DoS_UDP,
    df_mitm, df_recon_HostDiscovery, df_recon_OS, df_recon_pingsweep,
    df_recon_portscan, df_recon_vul_scan
], ignore_index=True)
df_all.to_csv('merged_dataset.csv', index=False)