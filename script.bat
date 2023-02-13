@chcp 1251
rmdir /s /q "C:\Users\Администратор\Desktop\converter\converted"
rmdir /s /q "C:\Users\Администратор\Desktop\converter\to_convert"
mkdir "C:\Users\Администратор\Desktop\converter\converted"
mkdir "C:\Users\Администратор\Desktop\converter\to_convert"

cd "C:\Users\Администратор\Desktop\converter"
uvicorn main:app --reload