import falcon
import os
# import uuid
# import mimetypes
# import json
from config.settings import config

class Collection(object):

    def __init__(self):
        # cfg = Configuration()
        # config = cfg.get_config()
        self.storage_path = config["storage"]["storage_path"]
        try:
            if not os.path.exists(self.storage_path):
                os.makedirs(self.storage_path)
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Storage Error',
                                   'Directory does not exist. <%s>' % self.storage_path)


    def on_post(self, req, resp, **kwargs):
        #student_id = kwargs["student_id"]

        student_id = "jcassid2@uotawa.ca"

        directory = os.path.join(self.storage_path, student_id)

        # TODO: Make the file storage if it does not exist - manage permission problem.
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except Exception:
            raise falcon.HTTPError(falcon.HTTP_500,
                                   'Storage Error',
                                   'Unable to create the directory: <%s>' % directory)
        
        print('come on!')

        # image = req.get_param('image')
        # # Read image as binary
        # raw = image.file.read()
        # # Retrieve filename
        # filename = image.filename
        print(kwarreq.get_param('title'))

        

        # for p in req.params:
        #     try:
        #         file = req.get_param(p)

        #         if not hasattr(file, 'filename'):
        #             raise falcon.HTTPInvalidParam('Invalid param', p)

        #         # Retrieve filename
        #         filename, ext = os.path.splitext(file.filename)

        #         filename = '{name}_{uuid}{ext}'.format(name=p, uuid=uuid.uuid4(), ext=ext)
        #         doc_path = os.path.join(self.storage_path, student_id, filename)
        #         with open(doc_path, 'wb') as doc_file:
        #             while True:
        #                 chunk = file.file.read(4096)
        #                 if not chunk:
        #                     break

        #                 doc_file.write(chunk)
        #     except Exception:
        #         raise falcon.HTTPError(falcon.HTTP_500,
        #                                'Storage Error',
        #                                'Unable to save document <%s>' % file.filename)

        resp.status = falcon.HTTP_201


#     def on_get(self, req, resp, **kwargs):
#         #return the list of documents for a student
#         student_id = kwargs["student_id"]
#         directory = os.path.join(self.storage_path, student_id)

#         files = [filename for filename in os.listdir(self.storage_path + '/' + student_id + '/')]
#         if files:
#             resp.body = json.dumps(files)
#         else:
#             raise falcon.HTTPError(falcon.HTTP_404,
#                 'File Error',
#                 'No document found.')


# class Item(object):
#     def __init__(self):
#         cfg = Configuration()
#         config = cfg.get_config()
#         self.storage_path = config["storage"]["storage_path"]

#     def on_get(self, req, resp, **kwargs):
#         name = kwargs["name"]
#         student_id = kwargs["student_id"]
#         try:
#             doc_path = os.path.join(self.storage_path, student_id, name)
#             if doc_path:
#                 resp.stream = open(doc_path, 'rb')
#                 resp.stream_len = os.path.getsize(doc_path)
#                 resp.content_type = 'application/octet-stream'
#         except Exception as e:
#             raise falcon.HTTPError(falcon.HTTP_500,
#                                        'File Error',
#                                        'Unable to open the document <%s>' % e)


if __name__ == "__main__": # running the module interactively
    print(config)
    print(config['storage'])
