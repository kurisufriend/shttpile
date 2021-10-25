from pathlib import Path
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
    @staticmethod
    def parse(raw):
        return int(raw.split[" "][0])
class query:
    def __init__(self):
        self.type = None #dol8r
        self.path = "/"
        self.vars = {}
    @staticmethod
    def get(status_line):
        q = query()
        q.type = status_line[0]
        q.path = status_line[1].split("?")[0]
        if len(status_line[1].split("?")) < 2: return q
        for v in status_line[1].split("?")[1].split("&"):
            var_arr = v.split("=")
            if type(var_arr) == str or v == "/":
                continue
            q.vars[var_arr[0]] = var_arr[1]
        return q
class headers:
    def __init__(self):
        self.headers_dict = {}
    def as_str(self):
        ret = ""
        for h in self.headers_dict:
            ret += h+": "+str(self.headers_dict[h])
            ret += "\r\n"
        return ret
class request:
    def __init__(self):
        self.status_line = []
        self.headers_obj = headers()
        self.body = ""
    def text(self):
        return " ".join(self.status_line)+"\r\n"+self.headers_obj.as_str()+"\r\n"+self.body
    @staticmethod
    def build_response(req):
        r = request()
        q = query.get(req.status_line.split(" "))

        r.status_line.append("HTTP/1.1")
        s_code = 200

        f = None
        try:
            query_path_obj = Path("."+q.path).resolve()
            jail = Path(".").resolve()
            if not(jail in query_path_obj.parents):
                r.body = ""
                s_code = 403
            else:
                f = open("."+q.path, "r+")
                r.body = f.read()
                f.close()

        except:
            r.body = ""
            s_code = 404

        # check if query is heckin cute % valid/returnable
        # always 200 for static testing
        status.add_status(r.status_line, s_code)

        # manual for now
        r.headers_obj.headers_dict["Server"] = "shttpile"
        r.headers_obj.headers_dict["Content-Type"] = "text/html"
        r.headers_obj.headers_dict["Content-Length"] = len(r.body.encode("ascii"))
        r.headers_obj.headers_dict["X-Clacks-Overhead"] = "GNU Terry Pratchett, Aaron Swartz, Norm Macdonald"

        return r
    @staticmethod
    def parse(raw):
        r = request()
        raw_lines = raw.split("\n")

        r.status_line = raw_lines[0]

        for line in raw_lines[1:]:
            if line == "\r":
                break
            header_line = line.split(": ")
            r.headers_obj.headers_dict[header_line[0]] = header_line[1]
        
        r.body = raw.split("\r\n\r\n")[1]

        return r