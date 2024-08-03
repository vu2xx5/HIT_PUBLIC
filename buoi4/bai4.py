import itertools

n = 4
input_set = {1, 2, 3, 4}
limit = 6

tap_hop_con_tot_nhat = set()
tong_tot_nhat = 0

tat_ca_to_hop = []
for r in range(len(input_set) + 1):
    tat_ca_to_hop.extend(itertools.combinations(input_set, r))

for to_hop in tat_ca_to_hop:
    tong_hien_tai = sum(to_hop)
    if tong_hien_tai <= limit and tong_hien_tai > tong_tot_nhat:
        tap_hop_con_tot_nhat = set(to_hop)
        tong_tot_nhat = tong_hien_tai

print(tap_hop_con_tot_nhat) 
