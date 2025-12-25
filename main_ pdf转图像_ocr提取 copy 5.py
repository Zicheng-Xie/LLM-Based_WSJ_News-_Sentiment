import pytesseract
from pdf2image import convert_from_path
import cv2
import re
import numpy as np

def extract_numbers_from_scanned_pdf(pdf_path, page_num, line_num, poppler_path):
    try:
             # 将PDF转换为图像
        images = convert_from_path(pdf_path, poppler_path=poppler_path)
        
        # 检查页码是否在范围内
        if page_num < 1 or page_num > len(images):
            return "页码超出范围"

        # 获取指定页的图像
        image = image[page_num - 1]  # 页码从0开始
        
        # 将PIL图像转换为OpenCV格式
        image_cv = cv2.cvtColor(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR), cv2.COLOR_BGR2GRAY)
        
        # 应用图像预处理，如阈值化，以提高OCR准确性
        image_cv = cv2.threshold(image_cv, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        
        # 使用OCR提取文本
        text = pytesseract.image_to_string(image_cv)
        lines = text.splitlines()
        
        # 检查行数是否在范围内
        if line_num < 1 or line_num > len(lines):
            return "行数超出范围"
        
        # 获取指定行的内容
        line_content = lines[line_num - 1]
        
        # 提取行中的数字
        numbers = re.findall(r'\d+', line_content)
        
        # 返回数字列表
        return numbers
    except Exception as e:
        return f"出现错误: {e}"

if __name__ == "__main__":
    # 输入PDF文件路径、页码和行数
    pdf_path = r"C:/Desktop/pypy_/111/图片2.png"
    page_num = int(input("请输入页码: "))
    line_num = int(input("请输入行数: "))

    poppler_path = r'D:\py\miniconda3\pkgs\poppler-24.07.0-h686f694_0\Library\bin'
    
    # 提取指定页码和行数中的数字
    result = extract_numbers_from_scanned_pdf(pdf_path, page_num, line_num, poppler_path)
    print(f"提取的数字: {result}")