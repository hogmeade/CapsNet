#!/usr/bin/env bash
#123 882 239 323 992
for seed in 239 323 992 123123 19897
    do
    CUDA_VISIBLE_DEVICES=0 python train.py --decoder=Conv --model 'cifar_conv_baseline_'$seed --seed $seed 
    python notify.py -m "se baseline" -s 'cifar_conv_baseline_'$seed
    done
