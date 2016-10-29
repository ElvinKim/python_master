def clip(text, max_len=80):

    end = None

    if len(text) > max_len:
        #rfind -> 뒤에서 부터 문자열을 찾고 그 index를 리턴
        space_before = text.rfind(" ", 0, max_len)

        if space_before >= 0 :
            end = space_before
        else:
            space_after = text.rfind(" ", max_len)
            if space_after >=0 :
                end = space_after

        if end is None:
            end = len(text)

        return text[:end].rstrip()




