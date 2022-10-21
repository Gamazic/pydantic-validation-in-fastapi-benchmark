#!/bin/bash

# uvicorn app:app --host 127.0.0.1 --port 8000 --reload

wrk "http://localhost:8000/sdr" -s post.lua -t 10 -c 10 -d 10s > results/sdr
wrk "http://localhost:8000/_s_dr" -s post.lua -t 10 -c 10 -d 10s > results/_s_dr
wrk "http://localhost:8000/_s_d_r" -s post.lua -t 10 -c 10 -d 10s > results/_s_d_r
wrk "http://localhost:8000/_sdr" -s post.lua -t 10 -c 10 -d 10s > results/_sdr

# num

wrk "http://localhost:8000/sdr/5" -s post.lua -t 10 -c 10 -d 10s > results/sdr_n5
wrk "http://localhost:8000/_sdr/5" -s post.lua -t 10 -c 10 -d 10s > results/_sdr_n5

# trans

wrk "http://localhost:8000/sdrt" -s post.lua -t 10 -c 10 -d 10s > results/sdrt
wrk "http://localhost:8000/s_drt" -s post.lua -t 10 -c 10 -d 10s > results/s_drt
wrk "http://localhost:8000/_s_drt" -s post.lua -t 10 -c 10 -d 10s > results/_s_drt
wrk "http://localhost:8000/_s_d_rt" -s post.lua -t 10 -c 10 -d 10s > results/_s_d_rt