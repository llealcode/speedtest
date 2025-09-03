import flet as ft
import speedtest
import threading
from time import sleep


def testar_animar(e, text_download, text_upload, text_ping):

    stop_event = threading.Event()

    def testar():
        st = speedtest.Speedtest()
        
        st.download()
        download = f'{st.results.download / 1_000_000:.0f} Mbps'
        text_download.value=download
        text_download.update()

        st.upload()
        upload = f'{st.results.upload / 1_000_000:.0f} Mbps'
        ping = f'{st.results.ping} Ms'
        text_upload.value=upload
        text_ping.value=ping
        text_upload.update()
        text_ping.update()
        
        stop_event.set() 

    def animar_botao(e):
    
        e.control.content.value='TESTANDO'
        e.control.bgcolor=ft.Colors.PINK

        while not stop_event.is_set():
            e.control.scale=ft.Scale(1.1)
            e.control.update()
            sleep(0.8)

            e.control.scale=ft.Scale(1)
            e.control.update()
            sleep(0.8)

        e.control.content.value='REFAZER'
        e.control.bgcolor=ft.Colors.YELLOW_800
        e.control.update()
        

    t1=threading.Thread(target=testar)
    t2=threading.Thread(target=animar_botao, args=[e])

    t1.start()
    t2.start()

    t1.join()
    t2.join()
