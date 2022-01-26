from traceback import print_tb
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from django.utils import timezone
from rest_framework import status
from django.conf import settings
import uuid

import logging
logger = logging.getLogger('mylogger')
# 批量創建目錄
def mkdirs_in_batch(path):
    try:
        path = os.path.normpath(path)  # 去掉路徑最右側的 \\ 、/
        path = path.replace('\\', '/') # 將所有的\\轉為/，避免出現轉義字串
        head, tail = os.path.split(path)
        if not os.path.isdir(path) and os.path.isfile(path):  # 如果path指向的是檔案，則分解檔案所在目錄
            head, tail = os.path.split(head)
 
        if tail == '': # head為根目錄，形如 / 、D:
            return True
 
        new_dir_path = ''  # 存放反轉后的目錄路徑
        root = ''  # 存放根目錄
        while tail:
            new_dir_path = new_dir_path + tail + '/'
            head, tail = os.path.split(head)
            root = head
        else:
            new_dir_path = root + new_dir_path
 
            # 批量創建目錄
            new_dir_path = os.path.normpath(new_dir_path)
            head, tail = os.path.split(new_dir_path)
            temp = ''
            while tail:
                temp = temp + '/' + tail
                dir_path = root + temp
                if not os.path.isdir(dir_path):
                    os.mkdir(dir_path)
                head, tail = os.path.split(head)
        return True
    except Exception as e:
        logger.error('批量創建目錄出錯：%s' % e)
        return False
class FileAPI(APIView):
    # 上傳附件
    def post(self, request, format=None):
        result = {}
        try:
            files = request.FILES
            file = files.get('photo')
            print(files,"---",file)
            if not file:
                result['msg'] =  '上傳失敗，未獲取到檔案'
                result['success'] =  False
                return Response(result, status.HTTP_400_BAD_REQUEST)
            file_name = file.name
            attachment_name = file_name
            creater = request.user.username
            create_time = timezone.now()
            time_str = create_time.strftime('%Y%m%d')
            name, suffix = os.path.splitext(file_name)
            file_name = str(uuid.uuid1()).replace('-', '') + time_str + suffix
            file_relative_path = "\\attachments\\"+ time_str
            file_absolute_path = str(settings.MEDIA_ROOT) + str(file_relative_path)
            print(file_absolute_path)
            if not os.path.exists(file_absolute_path):# 路徑不存在
                if not mkdirs_in_batch(file_absolute_path):
                        result['msg'] =  '批量創建路徑(%s)對應的目錄失敗' % file_absolute_path
                        result['success'] =  False
                        return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)
            file_relative_path += '/' + file_name
            file_absolute_path = file_absolute_path + '/' + file_name
            file_handler = open(file_absolute_path, 'wb')    # 打開特定的檔案進行二進制的寫操作
            try:
                for chunk in file.chunks():      # 分塊寫入檔案
                    file_handler.write(chunk)
            finally:
                file_handler.close()
            result['msg'] =  '上傳成功'
            result['success'] =  True
            return Response(result, status.HTTP_200_OK)

        except Exception as e:
                result['msg'] =  '%s' % e
                result['success'] =  False
                return Response(result, status.HTTP_500_INTERNAL_SERVER_ERROR)