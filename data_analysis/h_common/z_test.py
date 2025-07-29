from data_analysis.h_common.merge_multi_file import simple_append_merge_mutil_csv_file, \
    simple_append_merge_mutil_csv_file_with_selected_columns, aggregate_merge_multi_csv_files


def test_simple_append_merge_mutil_csv_file():
    # simple_append_merge_mutil_csv_file(
    #     "res/split",
    #     "res/temp/split-simple_append_merge_mutil_csv_file-merged.csv")

    # simple_append_merge_mutil_csv_file(
    #     "res/split",
    #     "res/temp/split-simple_append_merge_mutil_csv_file-merged-2.csv",
    #     [
    #         {"field": "service", "ascending": True},
    #         {"field": "serverIp", "ascending": True},
    #         {"field": "interface", "ascending": True},
    #         {"field": "userId", "ascending": False}
    #     ])

    # simple_append_merge_mutil_csv_file_with_selected_columns(
    #     "res/split",
    #     "res/temp/split-simple_append_merge_mutil_csv_file_with_selected_columns-merged.csv",
    #     ["service", "interface", "count"],
    #     [
    #         {"field": "service", "ascending": True},
    #         {"field": "interface", "ascending": True},
    #         {"field": "count", "ascending": False}]
    # )
    aggregate_merge_multi_csv_files(
        "res/split",
        "res/temp/split-aggregate_merge_multi_csv_files-merged.csv",
        ["service", "interface", "userId"],
        ["count"])


if __name__ == '__main__':
    test_simple_append_merge_mutil_csv_file()
