A Simple Flask Post Handler

Input: Image formats [png, jpg, jpeg]  
Output: JSON String {name, image_id, match_pct}    


Note:  
Image Files are stored in uploads folder(UPLOAD_FOLDER) in current directory   
Unique Image id is generated to store the image.  

Sample Usage  
Modify the path UPLOAD_FOLDER PATH to the required directory

$curl -F 'file=@/home/username/image.jpg' http://127.0.0.1:5000
 

