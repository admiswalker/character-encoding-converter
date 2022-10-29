import glob
import os

import text_reader_writer as trw


def main():
    print('hello')

    src_path = './input_files'
    dst_path = './output_files'
    
    l_path = glob.glob(src_path+'/**', recursive=True)
    
    for path_in in l_path:
        if os.path.isdir(path_in):
            continue
        
        path_out = dst_path+'/'+path_in.replace(src_path+'/', '', 1)
        path_out_dir = os.path.dirname(path_out)
        os.makedirs(path_out_dir, exist_ok=True)
        
        print(path_in)
        print(path_out)
        
        s = trw.read(path_in, encoding='utf-8-sig')
        print(s)
        trw.write(path_out, s, encoding='cp932')
        print()
    
    

main()

