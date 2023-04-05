# VishwaCTF_2023_Writeups
Our writeups for VishwaCTF 2023

## CID
- We are provided with an image `case69.jpg`. Nothing much in the picture, but reveals a password on checking metadata. Tried steghide with password, nothing
- Tried `binwalk`, reveals a `7z` file. Extracted it, and found several images with a text file. Text file of not much use
- All the images were of same size, except one `369.jpg`
- On applying `steghide` with the password found in metadata - ***"daya darwaza tod do"*** we get `flag.txt`
```
vishwaCTF{my_GOD_D4ya_tumn3_t0_fl4g_dhund_liy4....}
```

## My FOOLish Opponent
- The position given in the board and the title of the question suggests ***Fool's mate***
- The answer was one of the variations of the same
```
VishwaCTF{f3_e6_g4_Qh4#}
```

## 