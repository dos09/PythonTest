def fix_html(html):
    """ Adds "\r\n" to html in order to avoid the 990 line length limit
    
    SMTP servers chop lines longer than 990 symbols and insert new lines
    which can corrupt html.
    """
    def chop_str(str_data, chunk_width=500):
        chunks = []
        for i in range(0, len(str_data), chunk_width):
            chunks.append(str_data[i:i + chunk_width])
        return chunks

    def insert_crlf(input_str):
        """ Inserts "\r\n" in input_str on appropriate place.

        Appropriate place is considered before "</" or  after "/>".
        If no such place is found tries to insert before a space.
        Search is from end to start.
        If there is no suitable insertion position the input_str is 
        returned unmodified.
        """
        pos = input_str.rfind('</')
        if pos == -1:
            pos = input_str.rfind('/>')
            if pos == -1:
                pos = input_str.rfind(' ')
            else:
                pos += 2

        if pos != -1:
            return ''.join([input_str[:pos], '\r\n', input_str[pos:]])

        return input_str

    fixed = []
    for chunk in chop_str(html):
        fixed.append(insert_crlf(chunk))
    return ''.join(fixed)

print(fix_html('<b>asdadas afasf</b>'))
print(fix_html('<link .... />asdas'))