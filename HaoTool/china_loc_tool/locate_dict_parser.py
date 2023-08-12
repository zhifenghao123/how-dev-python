import jionlp as jio


def getLoc(request):
    loc_list = jio.read_file_by_line("../../HaoTool/dataset/loc_list.txt")
    print(loc_list)
    return loc_list


if __name__ == '__main__':
    getLoc(1)