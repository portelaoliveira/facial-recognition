import json

import cv2

from classes.simple_facerec import SimpleFacerec

# Dicionário para armazenar nome e foto
dados = {}


# def registrar_usuario():
#     # Acessar webcam
#     cap = cv2.VideoCapture(0)

#     # Contador para nomear as fotos
#     numero_foto = 0

#     while True:
#         # Ler frame da webcam
#         ret, frame = cap.read()

#         # Mostrar frame na tela
#         cv2.imshow("Registro Facial", frame)

#         # Verificar se a tecla 's' foi pressionada para salvar a foto
#         if cv2.waitKey(1) & 0xFF == ord("s"):
#             # Salvar foto
#             cv2.imwrite(f"images/foto_{numero_foto}.jpg", frame)

#             # Obter nome do usuário
#             nome = input("Digite seu nome: ")

#             # Adicionar dados ao dicionário
#             dados[f"foto_{numero_foto}.jpg"] = nome

#             # Salvar dicionário em arquivo JSON
#             with open("dados.json", "w") as f:
#                 json.dump(dados, f)

#             # Incrementar contador
#             numero_foto += 1

#             # Sair do loop
#             break

#     # Desligar webcam
#     cap.release()
#     cv2.destroyAllWindows()


# def reconhecimento_facial():
#     # Acessar webcam
#     cap = cv2.VideoCapture(0)

#     # Carregar dicionário de dados
#     with open("dados.json", "r") as f:
#         dados = json.load(f)

#     while True:
#         # Ler frame da webcam
#         ret, frame = cap.read()

#         # Mostrar frame na tela
#         cv2.imshow("Reconhecimento Facial", frame)

#         # Converter frame para grayscale
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Detectar faces no frame
#         faces = cv2.CascadeClassifier(
#             "haarcascade_frontalface_default.xml"
#         ).detectMultiScale(gray, 1.3, 5)

#         # Para cada face detectada
#         for x, y, w, h in faces:
#             # Extrair a região da face
#             face_roi = frame[y : y + h, x : x + w]

#             # Converter região da face para grayscale
#             face_roi_gray = cv2.cvtColor(face_roi, cv2.COLOR_BGR2GRAY)

#             # Comparar a face com as fotos do banco de dados
#             for foto, nome in dados.items():
#                 # Carregar foto do banco de dados
#                 foto_banco_dados = cv2.imread(f"banco_de_dados/{foto}")

#                 # Converter foto do banco de dados para grayscale
#                 foto_banco_dados_gray = cv2.cvtColor(
#                     foto_banco_dados, cv2.COLOR_BGR2GRAY
#                 )

#                 # Comparar as faces usando o método DeepFace
#                 resultado = DeepFace.compare_faces(
#                     face_roi_gray, foto_banco_dados_gray
#                 )

#                 # Se a comparação for bem-sucedida
#                 if resultado["confidence"] > 0.8:
#                     # Exibir mensagem de acesso permitido
#                     print("Acesso permitido")
#                     cv2.putText(
#                         frame,
#                         f"Acesso permitido: {nome}",
#                         (x, y - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         0.9,
#                         (0, 255, 0),
#                         2,
#                     )
#                 else:
#                     # Exibir mensagem de acesso negado
#                     print("Acesso negado")
#                     cv2.putText(
#                         frame,
#                         f"Acesso negado: {nome}",
#                         (x, y - 10),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         0.9,
#                         (0, 255, 0),
#                         2,
#                     )

#         # Verificar se a tecla 'q' foi pressionada para sair
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     # Desligar webcam
#     cap.release()
#     cv2.destroyAllWindows()


def registrar_usuario():
    # Acessar webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Ler frame da webcam
        ret, frame = cap.read()

        # Mostrar frame na tela
        cv2.imshow("Registro Facial", frame)

        # Verificar se a tecla 's' foi pressionada para salvar a foto
        if cv2.waitKey(1) & 0xFF == ord("s"):
            # Obter nome do usuário
            nome = input("Digite seu nome: ")

            # Salvar foto
            cv2.imwrite(f"images/{nome}.jpg", frame)

            # Sair do loop
            break

    # Desligar webcam
    cap.release()
    cv2.destroyAllWindows()


def reconhecimento_facial():
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                (0, 200, 0),
                2,
            )
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 4)

        cv2.imshow("Reconhecimento Facial", frame)

        # key = cv2.waitKey(1)
        # if key == 27:
        #     break

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


# Main menu
while True:
    print("1 - Registrar usuário")
    print("2 - Reconhecimento facial")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        registrar_usuario()
    elif opcao == 2:
        reconhecimento_facial()
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")
