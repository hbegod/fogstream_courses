import os.path
from collections import Counter

path_list = ['/dir0/bdemyqgvos.mp3', '/dir0/hcegpukmws.docx', '/dir0/dir1/dir2/yelzhvf.rty', '/dir1/dir0/hqazb.docx', '/dir1/dir0/dir2/resxkvwu.pdf', '/dir0/eskwxij.rty', '/dir2/dir1/dir0/udjzwomq.docx', '/dir0/baqpf.xcv', '/dir0/dir1/ptdckrngs.mp3', '/dir1/dir0/mewlpiv.pdf', '/dir1/dir0/ioxtulqmj.mp3', '/dir0/dkxbg.xcv', '/dir0/raidh.rty', '/dir1/dir0/dir2/xmras.mp3', '/dir0/dir1/dir2/yohjwbzuif.pdf', '/dir0/amxhtjw.pdf', '/dir2/dir1/dir0/omhznbgt.docx', '/dir0/dir1/fayuzvxlh.pdf', '/dir0/alftm.pdf', '/dir0/emktrhgdw.xcv', '/dir2/dir0/dir1/hbgrwx.rty', '/dir2/dir0/dir1/moyjwhxeb.rty', '/dir1/dir0/nlvdwhi.rty', '/dir0/dir1/dir2/clatpjqhn.rty', '/dir0/evinyhw.mp3', '/dir2/dir1/dir0/mpsjlv.rty', '/dir0/dir1/vfhetrca.docx', '/dir0/dir1/dir2/ijmhfe.rty', '/dir1/dir0/duzajnqxew.docx', '/dir1/dir0/dir2/dapmzrjg.pdf', '/dir0/wfoaulhe.rty', '/dir1/dir0/hlvkrbuo.pdf', '/dir0/fguzhqidlj.xcv', '/dir2/dir0/dir1/seaybvc.xcv', '/dir0/dir1/dir2/jgzusoae.rty', '/dir0/dir1/dir2/eznfoq.pdf', '/dir0/drbzp.docx', '/dir0/kuclvmy.docx', '/dir0/dir1/dir2/pofxwznujh.mp3', '/dir0/dir1/dir2/tirmlnv.rty', '/dir0/dir1/raqpc.xcv', '/dir1/dir0/yimulwnx.pdf', '/dir0/yawzjeg.pdf', '/dir1/dir0/emzap.rty', '/dir2/dir1/dir0/fpnjdzb.xcv', '/dir0/dir1/ftdwxhs.docx', '/dir2/dir0/dir1/ndahvges.mp3', '/dir0/uhyvcb.rty', '/dir1/dir2/dir0/rdevtjshmu.xcv', '/dir0/wdqvsr.docx', '/dir2/dir1/dir0/pmjgowylqe.docx', '/dir0/zmwgcasbpk.docx', '/dir1/dir0/iowxlf.xcv', '/dir0/gfzbai.docx', '/dir0/dir1/tfbaq.docx', '/dir0/pimjr.mp3', '/dir1/dir2/dir0/nczmvfye.rty', '/dir0/dir1/buihlwnsc.rty', '/dir0/ukmzfgbp.xcv', '/dir0/whuypc.xcv', '/dir0/dir1/lgvbutzy.xcv', '/dir0/hnilg.docx', '/dir0/kbtids.mp3', '/dir1/dir0/onyxfu.xcv', '/dir1/dir0/jguydbhxf.rty', '/dir1/dir0/xbznvtl.pdf', '/dir1/dir0/piatwqdskj.docx', '/dir0/sjtrypxbf.pdf', '/dir0/dir1/dir2/nyrvdkx.rty', '/dir0/dir2/dir1/xyfpu.docx', '/dir1/dir0/hakejqdlos.xcv', '/dir0/vnoughr.docx', '/dir0/mytzsp.docx', '/dir2/dir0/dir1/dqomcxzk.rty', '/dir0/qzijl.pdf', '/dir1/dir0/ajwsuz.pdf', '/dir0/ahdni.pdf', '/dir0/dir1/jxbceztp.docx', '/dir0/dir2/dir1/akloz.xcv', '/dir0/dir1/okafhj.rty', '/dir0/dir1/bwrzxfjum.pdf', '/dir0/dkowvhctus.pdf', '/dir0/shxmlyg.xcv', '/dir1/dir0/njlci.pdf', '/dir2/dir1/dir0/xlykg.rty', '/dir0/pyanxhrmgc.docx', '/dir1/dir2/dir0/azrqwg.xcv', '/dir1/dir0/jndxc.xcv', '/dir0/dir1/eqabzlmxdk.docx', '/dir0/dir1/dir2/vhqerlnwf.rty', '/dir0/owysngex.docx', '/dir0/dir1/kshpmtr.xcv', '/dir0/dir1/kwmygxn.docx', '/dir0/kmujiywvn.docx', '/dir1/dir0/alozyqds.xcv', '/dir0/ywklg.rty', '/dir1/dir2/dir0/cjeftgvpn.xcv', '/dir0/ijychs.mp3', '/dir1/dir0/dir2/fqgomldur.pdf', '/dir0/pskjmh.mp3']


def count_file_extensions(paths_to_files):
    """
    Returns dict with counted file extensions
    :param paths_to_files: list with paths
    :return: dict
    """
    file_extensions_list = []
    for path in paths_to_files:
        file_extensions_list.append(os.path.splitext(path)[1])
    return Counter(file_extensions_list)


result = count_file_extensions(path_list)
