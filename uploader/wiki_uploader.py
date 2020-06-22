import logging
import uuid

import mwclient


class WikiUploader(object):
    mw_client = None

    def __init__(
        self,
        host=None,
        consumer_secret=None,
        consumer_token=None,
        access_token=None,
        access_secret=None,
    ):
        self.mw_client = mwclient.Site(
            host=host,
            consumer_secret=consumer_secret,
            consumer_token=consumer_token,
            access_token=access_token,
            access_secret=access_secret,
        )

    def upload_file(self, file_name, file_stream, description="", license=""):
        if not description:
            description = file_name

        upload_result = self.mw_client.upload(
            file=file_stream,
            filename=file_name,
            description=description,
            date_created = date_created,
            ignore=True,
<<<<<<< HEAD
            comment=get_initial_page_text(date_created, description),
=======
            comment=get_initial_page_text(license, description),
>>>>>>> Add license picker for each file and implemented get_initial_page_text function
        )
        debug_information = "Uploaded: {0} to: {1}, more information: {2}".format(
            file_name, self.mw_client.host, upload_result
        )
        logging.debug(debug_information)
        upload_response = upload_result.get("result")
        if not upload_response == "Success":
            return False, {}
        else:
            return True, upload_result["imageinfo"]

<<<<<<< HEAD
def get_initial_page_text(date_created="", summary=""):

    return """=={{{{int:filedesc}}}}==
{{{{Information|
{{{{en|{0}}}}}
}}}}
=={{{{int:license-header}}}}==
{{{{{1}}}}}
[[Category:{2}]] 
""".format(
        summary, date_created
    )   
=======

def get_initial_page_text(license="", summary=""):

    return "== Summary ==\n{0}\n== Licensing ==\n{{{{{1}}}}} ".format(summary, license)
>>>>>>> Add license picker for each file and implemented get_initial_page_text function
