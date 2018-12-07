import os.path


files_heap = ['bucima.rty', 'kqlvoys.sedf', 'yjoka.rty', 'hqmec.sedf', 'kwunl.rty', 'cfuomjn.rty', 'qdreugj.sedf', 'qmwpkl.rty', 'kngmopaju.sedf', 'qirfxukpw.rty', 'hxcrwlpd.sedf', 'cwmgbds.rtf', 'uonjlrgcm.sedf', 'gnhdsfykrw.rtf', 'oyuatlhqkf.rty', 'mtxoqbeifw.sedf', 'nkhmiv.rty', 'bhpav.rtf', 'odcvikfm.sedf', 'dsumjhaikl.sedf', 'mugca.rty', 'arjdh.rty', 'dyfavrgbk.sedf', 'qkceg.sedf', 'lifux.rtf', 'mzphgsyxj.rtf', 'qijdo.rty', 'aqhycdpz.rtf', 'fnqbmoe.rty', 'dsvyjicngm.rtf', 'jwotuaiz.sedf', 'asdxgwq.rtf', 'pzrghoda.rtf', 'duqrzjft.rtf', 'nwcpykloht.rtf', 'fsaethjvg.rty', 'suhbcx.rty', 'munqt.rty', 'uochlfmn.sedf', 'zwjosmuhig.rty', 'czyewgnhv.sedf', 'ayomsduec.rtf', 'wbxfdj.sedf', 'xvfdhoung.rty', 'ibvrhseqc.rty', 'vnplemg.sedf', 'vuomlex.rty', 'lpxmk.sedf', 'vpothagxzn.rtf', 'fmjhxuvwsc.rtf', 'liouzmbthp.sedf', 'kslve.rtf', 'xylgb.rtf', 'bslcktfw.rty', 'kyino.sedf', 'drpmbkogy.rtf', 'zxhca.rtf', 'ewfzsrm.rty', 'bqvpju.rty', 'flhoyi.rty', 'jzdop.rty', 'oznqfgrx.sedf', 'suqkay.rty', 'uckmhznot.rtf', 'dwcahyef.sedf', 'zgucfith.rty', 'fwrhzgtia.rty', 'iequj.rty', 'ylbcwjnd.rtf', 'qytcuelwnk.rtf', 'tkpbshdro.sedf', 'bunvjycel.rtf', 'cksqdopnb.rty', 'zmdbopr.rty', 'ejainr.rty', 'rghcjumf.sedf', 'pvgwq.rty', 'tyjhg.sedf', 'ftosnemwq.rty', 'phtgqjlni.sedf', 'cwrfvo.rtf', 'nifgxqh.rtf', 'grnsqpdyh.sedf', 'lueoa.rtf', 'kdvtpjzhcl.rtf', 'tmhlpau.rty', 'cekuwstdxm.rtf', 'lbramxsugt.rty', 'rhkevti.rtf', 'ukrpondi.sedf', 'ymbjwuico.sedf', 'kzurwvpnit.rtf', 'ygknxwjpl.rtf', 'ibymcx.sedf', 'djkfir.sedf', 'mdvburnqi.rtf', 'jemotvd.rtf', 'rlztj.sedf', 'dqrpjo.rtf', 'bgqdavwos.rty']
path_map = {'.rty': 'dir1/dir0', '.sedf': 'dir1/dir2/dir0', '.rtf': 'dir1/dir2/dir0'}


def generate_full_paths_for_files(list_of_files, dict_of_path_for_extensions):
    """
    Joins filename from list with the path for file extension from dict
    :param list_of_files: list of file names
    :param dict_of_path_for_extensions:  dict with path for extensions where extension is a key and
    path is a value
    :return: list of generatied full pats
    """
    result_list = []
    for file in list_of_files:
        result_list.append(
            os.path.join(
                dict_of_path_for_extensions.get(
                    os.path.splitext(file)[1]), file
            )
        )
    return result_list


result = generate_full_paths_for_files(files_heap, path_map)
print(result)