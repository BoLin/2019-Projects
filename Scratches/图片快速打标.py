
import os
import cv2
import json
import time

if __name__ == "__main__":
    root = os.getcwd()
    final= {}
    count = 1
    for name in os.listdir(root):
        try:
            if os.path.splitext(name)[-1].lower() in [".jpg",".png"]:
                print(count,name)
                image = cv2.imread(name)
                cv2.namedWindow("Picture", 0)
                cv2.resizeWindow("Picture", 400, 400)
                cv2.imshow("Picture",image)
                cv2.waitKey(1000)

                result = input()
                for i in result:
                    try:
                        final[i]
                        final[i].append(name)
                    except:
                        final[i] = [name]
                cv2.destroyAllWindows()
        except Exception as e:
            print(e)
        count += 1
        if count % 100 == 0:
            print("已经打标100张，备份结果中...")
            with open("result.json", 'w') as rec:
                json.dump(final, rec)
            for num in final:
                print("第", str(num), "类有 ：", str(len(final[num])), "张")


    with open("result.json", 'w') as rec:
        json.dump(final, rec)
    print("程序完成....")
    for num in final:
        print("第", str(num),"类有 ：",str(len(final[num])),"张")
    time.sleep(10)



