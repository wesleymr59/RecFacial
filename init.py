import cv2, os

# Funcao para busca de arquivos
def find(name, path):
    for root, dirs, files in os.walk(path):
        if (name in files) or (name in dirs):
            print("O diretorio/arquivo {} encontra-se em: {}".format(name, root))
            return os.path.join(root, name)
    # Caso nao encontre, recursao para diretorios anteriores
    return find(name, os.path.dirname(path))


# Importar arquivo XML
try:
    cv2path = os.path.dirname(cv2.__file__)
    haar_path = find('haarcascade_frontalface_alt2.xml', cv2path)
    xml_name = 'haarcascade_frontalface_alt2.xml'
    xml_path = os.path.join(haar_path, xml_name)

except ValueError:
    print('error')


# Inicializar Classificador
clf = cv2.CascadeClassifier("/home/wesley/Documentos/RecFacial/haarcascade_frontalface_alt2.xml")

# Inicializar webcam
cap = cv2.VideoCapture(0)

while(not cv2.waitKey(20) & 0xFF == ord('q')):

        # Capturar proximo frame
        ret, frame = cap.read()

        # Converter para tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Classificar
        faces = clf.detectMultiScale(gray)

        # Desenhar retangulo
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0))

        # Visualizar
        img = cv2.imshow('frame',frame)

        current_frame = 0
        if cv2.waitKey(20) == ord("s"): # se s for pressionado salva a imagem
            while True:
                if cap.isOpened():
                    current_frame = 0
                    if ret:
                        name = f'{current_frame}.jpg'
                        print(f"Creating file... {name}")
                        cv2.imwrite(name, frame)
                    current_frame += 1
                    cap.release()

cap.release()
cv2.destroyAllWindows()