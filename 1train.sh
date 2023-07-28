#!/usr/bin/env bash
for seed in 89796769 6873437 9898997 766776
    do
    CUDA_VISIBLE_DEVICES=1 python train.py --decoder=Conv --model 'cifar_conv_baseline_'$seed --seed $seed 
    python notify.py -m "se baseline" -s 'cifar_conv_baseline_'$seed
    done
