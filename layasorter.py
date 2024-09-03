import flet as ft
import os
from sort_module import Sorter

# Color Palette
electro_yellow = '#f5f096'
electro_dark = '#2a2927'
electro_dark_accent = '#221f1d'
electro_light = '#f3efe9'
electro_gray = '#8f8c89'

def main(page: ft.Page):
    page.title = "Layasorter: Manyland Sprite Sorter"
    page.bgcolor = electro_dark
    page.window.width = 768
    page.window.height = 320
    page.window.icon = "favicon.png"

    def disable_components():
        laya_source_textfield.disabled = True
        laya_destination_textfield.disabled = True
        laya_source_folder.disabled = True
        laya_destination_folder.disabled = True
        laya_sort_button.disabled = True

        laya_source_textfield.update()
        laya_destination_textfield.update()
        laya_source_folder.update()
        laya_destination_folder.update()
        laya_sort_button.update()
    
    def enable_components():
        laya_source_textfield.disabled = False
        laya_destination_textfield.disabled = False
        laya_source_folder.disabled = False
        laya_destination_folder.disabled = False
        laya_sort_button.disabled = False

        laya_source_textfield.update()
        laya_destination_textfield.update()
        laya_source_folder.update()
        laya_destination_folder.update()
        laya_sort_button.update()


    def pick_source_path(e: ft.FilePickerResultEvent):
        laya_source_textfield.value = e.path
        laya_source_textfield.update()
    
    def pick_destination_path(e: ft.FilePickerResultEvent):
        laya_destination_textfield.value = e.path
        laya_destination_textfield.update()
    
    def run_sorter(e):
        efl = [] # exception flag
        laya_error.controls = []
        if not os.path.exists(laya_source_textfield.value):
            efl.append("Source directory")
        
        if not os.path.exists(laya_destination_textfield.value):
            efl.append("Destination directory")

        if len(efl) == 0:
            laya_error.update()
            disable_components()
            sorter = Sorter(source_folder=laya_source_textfield.value, target_folder=laya_destination_textfield.value)
            sorter.read_data()
            sorter.get_spritetype()
            enable_components()
        else:
            enable_components()
            for ex in efl:
                laya_error.controls.append(ft.Text(value=f"{ex} is not a valid directory!", color="#e6b9d5", size=8))
        
        laya_error.update()
        
    
    pick_source_dialog = ft.FilePicker(on_result=pick_source_path)
    pick_destination_dialog = ft.FilePicker(on_result=pick_destination_path)
    laya_source_textfield = ft.TextField(hint_text="Enter a file path.", 
                                         fill_color=electro_dark_accent, 
                                         color=electro_light, 
                                         hint_style=ft.TextStyle(size=9, color=electro_gray),
                                         border_color=electro_yellow, 
                                         border_width=1, 
                                         height=24,
                                         expand_loose=True,
                                         text_size=11, 
                                         border_radius=25,
                                         text_vertical_align=ft.VerticalAlignment.CENTER,
                                         )
    laya_destination_textfield = ft.TextField(hint_text="Enter a file path.", 
                                         fill_color=electro_dark_accent, 
                                         color=electro_light, 
                                         hint_style=ft.TextStyle(size=9, color=electro_gray),
                                         border_color=electro_yellow, 
                                         border_width=1, 
                                         height=24,
                                         expand_loose=True,
                                         text_size=11, 
                                         border_radius=25,
                                         text_vertical_align=ft.VerticalAlignment.CENTER,
                                         )
    laya_source_folder = ft.Container(content=ft.Image(src='laya_folder.png'),
                                      width=20, height=20, image_fit=True, bgcolor=ft.colors.TRANSPARENT, ink=True, margin=ft.margin.only(right=4), border_radius=100,
                                      on_click=lambda e: pick_source_dialog.get_directory_path(dialog_title="Select Source Directory"))
    laya_destination_folder = ft.Container(content=ft.Image(src='laya_folder.png'),
                                           width=20, height=20, image_fit=True, bgcolor=ft.colors.TRANSPARENT, ink=True, margin=ft.margin.only(right=4), border_radius=100,
                                           on_click=lambda e: pick_destination_dialog.get_directory_path(dialog_title="Select Destination Directory"))
    
    laya_sort_button = ft.Container(
        content=ft.Text("Sort", color=electro_dark, font_family="centurygothic.ttf", weight=ft.FontWeight.W_600, size=16), 
        padding=ft.padding.symmetric(horizontal=32, vertical=2), border_radius=16, border=ft.border.all(2, electro_yellow), ink=True,
        gradient=ft.LinearGradient(begin=ft.alignment.top_left, end=ft.alignment.bottom_right, colors=[
            "#e9e596", "#e6b9d5"
        ]),
        on_click=run_sorter
    )
    laya_error = ft.Column([], spacing=0)
    
    page.overlay.append(pick_source_dialog)
    page.overlay.append(pick_destination_dialog)
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    # Header
                    ft.Row(
                        [
                            ft.Image(src="layazero.png", width=50, height=50),
                            ft.Text("LAYASORTER", font_family="centurygothic.ttf", color=electro_yellow, size=32)
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),

                    # Body
                    ft.Container(
                        content=ft.Column([
                            ft.Row(
                                [
                                    ft.Text("Source Folder:", font_family="centurygothic.ttf", color=electro_light, size=16),
                                    ft.Stack([laya_source_textfield, laya_source_folder], alignment=ft.alignment.center_right, expand=True)
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row(
                                [
                                    ft.Text("Destination Folder:", font_family="centurygothic.ttf", color=electro_light, size=16),
                                    ft.Stack([laya_destination_textfield, laya_destination_folder], alignment=ft.alignment.center_right, expand=True)
                                ],
                                alignment=ft.MainAxisAlignment.START,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            ft.Row([
                                laya_sort_button
                            ],alignment=ft.MainAxisAlignment.END
                            ),
                            laya_error
                        ]),
                        margin=ft.margin.only(top=8),
                        padding=ft.padding.symmetric(horizontal=16),
                    )
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.START,
            ), padding=ft.padding.symmetric(horizontal=32, vertical=8), alignment=ft.alignment.center
        )
        
    )

ft.app(target=main, assets_dir="assets")