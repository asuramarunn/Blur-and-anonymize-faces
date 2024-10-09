# Dự án gồm 2 file là ultis và gui. 
- Trong đó, ultis bao gồm các hàm:
    - detect_faces: sử dụng để nhận diện khu vực có mặt.
    - blur_faces: hàm làm mờ mặt.
    - pixelize_image: hàm pixel hóa gương mặt.
    - replace_face_with_icon: hàm thay thế icon vào gương mặt.
    -  process_image: hàm xử lý ảnh theo yêu cầu đầu vào.
    - process_video: hàm xử lý video theo yêu cầu đầu vào.
    - stream_from_camera: hàm xử lý đầu vào video trực tiếp theo yêu cầu đầu vào.
- Các hàm trong file ultis có tác dụng nhận diện và xử lý các phép biến đổi trong khuôn mặt đối tượng thu được.

- File gui lưu trữ 1 giao diện người dùng cơ bản:
    - Chứa 3 button với các mục đích để lựa chọn đẩy ảnh, video hay sử dụng trực tiếp từ camera.
    - Một thanh điều chỉnh độ mờ của blur.
    - Một hộp chọn phép biến đổi muốn áp dụng lên ảnh.
    - 1 nút dùng để up ảnh có tác dụng thay thế lên khuôn mặt tìm được.
