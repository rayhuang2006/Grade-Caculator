#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:31:24 2022

version 1.0.0
@author: rayhuang
"""

#如果你是一類組 請解開下半部分一類組的註解
#二三類組依據自己的需求 解開相對應註解

chinese = int(input("請輸入國文成績："))
math = int(input("請輸入數學成績："))
english = int(input("請輸入英文成績："))
physics = int(input("請輸入物理成績："))
chemistry = int(input("請輸入化學成績："))
civic = int(input("請輸入公民成績："))
geo = int(input("請輸入地理成績："))
bio = int(input("請輸入生物成績："))
his = int(input("請輸入歷史成績："))
ear = int(input("請輸入地科成績："))

#score = str(float((chinese *4 + math *4 + english *4 + civic *2 + geo *2 + his *2)/18)) #一類組
#score = str(float((chinese *4 + math *4 + english *4 + physics *2 + chemistry *2 + civic *2 + geo *2 + bio *2)/22)) # 高二 三類組下學期 二類組上學期
#score = str(float((chinese *4 + math *4 + english *4 + physics *2 + chemistry *2 + his *2 + bio *2)/20)) # 高二 二類組下學期 三類組下學期

print("你的成績是：" + score)
