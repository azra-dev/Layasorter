from PIL import Image
import os
import shutil
import json

class Sorter:
    def __init__(self, source_folder='meteos', target_folder='meteos_sorted'):
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.json_list = []
        self.img_list = []
        
    
    def read_data(self):
        source_path = os.path.join(self.source_folder, 'creations')
        temp_all_paths = []
        for file in os.listdir(source_path):
            file_path = os.path.join(source_path, file)
            temp_all_paths.append(file_path)
        
        temp_all_paths.sort()

        matching_json_file = None
        matching_filename = None
        for file in temp_all_paths:
            filename, ext = str.split(file, '.')
            if ext in ['json']:
                matching_json_file = file
                matching_filename = filename
            elif ext in ['png'] and filename == matching_filename:
                self.json_list.append(matching_json_file)
                self.img_list.append(file)

        print(f"JSON: {len(self.json_list)}, IMAGE: {len(self.img_list)}")


    def get_spritetype(self):
        idx = 0
        for sprite in self.json_list:
            try:
                f = open(sprite)
                sprite_json = json.load(f)
                sprite_type = sprite_json['base']
                sprite_path = os.path.join(self.target_folder, sprite_type)
                
                if not os.path.exists(sprite_path):
                    os.makedirs(sprite_path)
                
                if sprite_type in ['HOLDER']:
                    sprite_id = sprite_json['id']
                    sprite_name = sprite_json['name'].replace(" ", "_")
                    holder_path = os.path.join(sprite_path, f"{sprite_name}-{sprite_id}")
                    if not os.path.exists(holder_path):
                        os.makedirs(holder_path)
                    
                    shutil.copy(self.img_list[idx], holder_path)

                    # Access Holder's Json
                    source_holder_filename = ".".join((sprite_id, 'json'))
                    source_holder_path = os.path.join(self.source_folder, 'holders', source_holder_filename)
                    g = open(source_holder_path)
                    holder_json = json.load(g)
                    for item in holder_json['contents']:
                        item = item['itemId']
                        item_filename = ".".join((item, 'png'))
                        item_path = os.path.join(self.source_folder, 'creations', item_filename)
                        shutil.copy(item_path, holder_path)
                else:
                    # shutil.copy(self.img_list[idx], sprite_path)
                    None

            except:
                print("Invalid Operation.")
            
            idx+=1

def main():
    source_folder = 'meteos'
    target_folder = 'meteos_sorted'

    sorter = Sorter(source_folder=source_folder, target_folder=target_folder)
    sorter.read_data()
    sorter.get_spritetype()

if __name__ == '__main__':
    main()