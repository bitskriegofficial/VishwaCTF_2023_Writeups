# VishwaCTF-2023 Writeups
Our writeups for VishwaCTF 2023<br><br>
Team Name - **BITSkrieg**<br>
Rank - **#6/1090**<br>
Flags - **28/47**<br>
First Bloods - **3**<br>
Points - **7118**

## I am an Investigator
- We are given a corrupted image `RealFirst.png`. As we can see the header reads `BHAI` :)
- I fixed the magic bytes to `89 50 4E 47` and got the image
- The image talks about ***Latitude*** & ***Longitude*** as being the length and breadth of the image respectively **(in cm)**
- I checked the metadata of the image using `exiftool`
- We get size of image as `6186 x 614` & resolution as `118.1098901`

$Latitude = \frac{6186}{118.1098901} = 52.3749$
<br>

$Longitude = \frac{614}{118.1098901} = 5.1985$

- On entering these values on Google Maps, we landed up somewhere in Netherlands
- I checked out `Beatrixpark Dock` cause it seemed the nearest tourist attraction & I found a review by `vishwa_crimebranch`
- As it said, I went to the instagram with the same username & found a Drive link in the post, it contained a `.mp4` video with a very small width
-
```

```

## Super23
```

```

## Email Incoming
```

```

## Nice guys finish last
```

```

## Quick Heal
```

```

## Reversing is Ezeeee....
```

```

## Eeezzy
```

```

## Phi-Calculator
```

```

## Guatemala
```

```

## Mystery of Oakville Town
```

```

## The Sender Conundrum

```

```

## 1nj3ct0r
```

```

## Just Files
```

```

## Privacy Breach

```

```
