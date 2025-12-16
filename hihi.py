def baitap1():
 print("=== PHÂN TÍCH DÃY SỐ (KHÔNG LƯU TOÀN BỘ DÃY) ===")
# --- Bước 1: Nhập số lượng phần tử ---
 while True:
    try:
        N = int(input("Nhập số lượng phần tử N (số nguyên dương): "))
        if N > 0:
            break
        else:
            print("N phải lớn hơn 0. Vui lòng nhập lại.")
    except:
        print("Giá trị không hợp lệ. Hãy nhập một số nguyên dương.")
# --- Khởi tạo biến trạng thái ---
 sum_val = 0
 even_count = 0
 count = 0
 max_val = None
 min_val = None
 print(f"\nHãy nhập {N} số nguyên:")
# --- Bước 2: Dùng 1 vòng lặp duy nhất để nhập toàn bộ N số ---
 while count < N:
    try:
        value = int(input(f"Nhập số thứ {count+1}: "))
    except:
        print("Lỗi: Hãy nhập một số nguyên!")
        continue
    # Cập nhật sum
    sum_val += value
    # Cập nhật max, min
    if max_val is None or value > max_val:
        max_val = value
    if min_val is None or value < min_val:
        min_val = value
    # Đếm số chẵn
    if value % 2 == 0:
        even_count += 1
    count += 1
# --- Bước 3: Tính trung bình ---
 average = sum_val / N
# --- Bước 4: Xuất kết quả ---
 print("\n===== KẾT QUẢ PHÂN TÍCH =====")
 print("Số lớn nhất:", max_val)
 print("Số nhỏ nhất:", min_val)
 print("Giá trị trung bình:", average)
 print("Số lượng số chẵn:", even_count)
 print("==============================")
 print("kết quả này có làm bạn hài lòng không?")
 print("nếu hài lòng thì cho mình 5* nhé hihi.")
if __name__ == "__main__":
    baitap1()
