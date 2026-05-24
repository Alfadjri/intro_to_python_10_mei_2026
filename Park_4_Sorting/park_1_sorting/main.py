import random
def generate_random_number(jumlah:int):
    list_data = []
    for index in range(jumlah):
        value = random.randint(1,100)
        list_data.append(value)
    return list_data

def bobble_sorting(data:list):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        for index_value in range(0,jumlah_data-index-1):
            if data[index_value] > data[index_value + 1]:
                tmp = data[index_value]
                data[index_value] = data[index_value + 1]
                data[index_value + 1] = tmp
def selecting_sorting(data:list):
    jumlah_data = len(data)
    for index in range(jumlah_data):
        min_index = index 
        for index_value in range(index + 1 , jumlah_data):
            if data[index_value] < data[min_index]:
                 min_index = index_value
        # tmp = data[index]
        # data[index] =data[min_index]
        # data[min_index] = tmp 
        data[index],data[min_index] = data[min_index],data[index]

def insert_sorting(data:list):
    for index in range(1,len(data)):
        min_value_index = data[index]
        index_value = index - 1
        while index_value >= 0 and min_value_index < data[index_value]:
            data[index_value + 1] = data[index_value]
            index_value -= 1
        data[index_value + 1] = min_value_index

def merge_sorting(data:list):
    if len(data) > 1 :
        nilai_tengah = len(data) // 2
        data_kiri = data[:nilai_tengah]
        data_kanan = data[nilai_tengah:]
        merge_sorting(data_kiri)
        merge_sorting(data_kanan)
        index = 0
        index_value = 0 
        real_index = 0

        while index < len(data_kiri) and index_value < len(data_kanan):
            if data_kiri[index] < data_kanan[index_value]:
                data[real_index] = data_kiri[index]
                index += 1
            else:
                data[real_index] = data_kanan[index_value]
                index_value += 1
            real_index += 1
        
        while index < len(data_kiri):
            data[real_index] = data_kiri[index]
            index += 1
            real_index +=1
        while index_value < len(data_kanan):
            data[real_index] = data_kanan[index_value]
            index_value += 1
            real_index += 1


def main():
    jumlah_data = int(input("Masukan jumlah data : "))
    data = generate_random_number(jumlah_data)
    print("===List sebelum di urutkan===")
    print(f"{data}")
    # start time
    # bobble_sorting(data)
    # selecting_sorting(data)
    # insert_sorting(data)
    merge_sorting(data)
    print("===List setelah di urutkan (ASC)")
    print(f"{data}")
    # end time

if __name__ == "__main__":
    main()