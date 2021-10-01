class status:
    all_valid = { # https://www.w3.org/Protocols/rfc2616/rfc2616-sec6.html
        200: "OK",# add the rest l8r
        403: "Forbidden",
        404: "Not Found",
        500: "Internal Server Error",
        505: "HTTP Version not supported"
    }
    def __init__(self):
        pass
    @staticmethod
    def add_status(status_line, code):
        status_line.append(str(code)+" "+status.all_valid[code])
class headers:
    def __init__(self):
        self.headers_dict = {}
    def as_str(self):
        ret = ""
        for h in self.headers_dict:
            ret += h+": "+str(self.headers_dict[h])
            ret += "\r\n"
        return ret
class response:
    def __init__(self):
        self.status_line = []
        self.headers_obj = headers()
        self.body = ""
    def text(self):
        return " ".join(self.status_line)+"\r\n"+self.headers_obj.as_str()+"\r\n"+self.body
    @staticmethod
    def build(query):
        r = response()

        r.status_line.append("HTTP/1.1")
        # check if query is heckin cute % valid/returnable
        # always 200 for static testing
        status.add_status(r.status_line, 200)
        
        f = open(query, "r")
        r.body = f.read()
        f.close()

        # manual for now
        r.headers_obj.headers_dict["Server"] = "shttpile"
        r.headers_obj.headers_dict["Content-Type"] = "text/html"
        r.headers_obj.headers_dict["Content-Length"] = len(r.body.encode("ascii"))
        r.headers_obj.headers_dict["X-Clacks-Overhead"] = "GNU Terry Pratchett, Aaron Swartz, Norm Macdonald"

        return r
