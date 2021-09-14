# Basic-DIP
## Repository này được chia làm bốn chủ đề chính:
- [Rotate Image](https://github.com/huynth1801/Basic-DIP/blob/master/README.md#rotate-image)
- [Background Subtraction](https://github.com/huynth1801/Basic-DIP/blob/master/README.md#background-subtraction)
- [Tìm kiếm hình ảnh tương tự bằng Cosine Similarity đơn giản](https://github.com/huynth1801/Basic-DIP/blob/master/README.md#cosine-similarity)
- [Disparity maps](https://github.com/huynth1801/Basic-DIP/blob/master/README.md#basic-disparity-map)


## Rotate Image


## Background Subtraction
Bước 1: Chúng ta tiền xử lý ảnh về cùng size, làm mờ ảnh bằng bộ lọc Gaussian.

Bước 2: Lấy 2 ảnh trừ nhau ở đây là lấy ảnh Observed Image trừ cho ảnh Background, chuyển ảnh sang gray nếu giá trị tại một vị trí pixel > threshold thì coi đây là object, ta gán giá trị cho nó là 255, tức là màu trắng ngược lại gán 0 (màu đen)

Bước 3: Thực hiện invert mask

Bước 4: Sử dụng mask để trích xuất các phần liên quan giữa Foreground và Background


## Cosine Similarity


## Basic Disparity Map
