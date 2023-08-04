#!/usr/bin/env bash
<<<<<<< HEAD
# 882 239 323 992 123123 19897 89796769 6873437 9898997 766776
for seed in 239 323 992 123123 19897 89796769 6873437 9898997 766776
    do
    CUDA_VISIBLE_DEVICES=1 python train.py --decoder=FC --model 'cifar_fc_24_no_v_'$seed --seed $seed --save_images
    python notify.py -m "se baseline" -s 'cifar_conv_baseline'$seed
    done
=======
for seed in 89796769 6873437 9898997 766776
    do
    CUDA_VISIBLE_DEVICES=1 python train.py --decoder=Conv --model 'cifar_conv_baseline_'$seed --seed $seed 
    python notify.py -m "se baseline" -s 'cifar_conv_baseline_'$seed
    done
>>>>>>> 3bb7c4d81f418f7639edaa41423c81f3c2e93e4b
