import cv2 as cv
from time import time,sleep
from modules.windowcapture import WindowCapture
from modules.bot import Brawlbot, BotState
from modules.screendetect import Screendetect, Detectstate
from modules.detection import Detection
from modules.print import bcolors
import pyautogui as py
import os
from constants import Constants

def stop_all_thread(wincap,screendetect,bot,detector):
    """
    stop all thread from running
    """
    py.mouseUp(button = Constants.movement_key)
    wincap.stop()
    detector.stop()
    screendetect.stop()
    bot.stop()
    cv.destroyAllWindows()

def add_two_tuple(tup1,tup2):
    """
    add two tuples
    """
    if not(tup1 is None or tup2 is None):
        return tuple(map(sum, zip(tup1, tup2)))

def main():
    # initialize the WindowCapture class
    wincap = WindowCapture(Constants.window_name)
    # get window dimension
    windowSize = wincap.get_dimension()
    # set target window as foreground
    sleep(0.5)
    wincap.set_window()

    # initialize detection class
    detector = Detection(windowSize,Constants.model_file_path,Constants.classes,Constants.heightScaleFactor)
    # initialize screendectect class
    screendetect = Screendetect(windowSize,wincap.offsets)
    # initialize bot class
    bot = Brawlbot(windowSize, wincap.offsets, Constants.speed, Constants.attack_range)
    
    # move cursor to the middle of bluestacks
    middle_of_window = (int(wincap.w/2+wincap.offset_x),int(wincap.h/2+wincap.offset_y))
    py.moveTo(middle_of_window[0],middle_of_window[1])

    #start thread
    wincap.start()
    detector.start()
    screendetect.start()
    
    print(f"Çözünürlük: {wincap.screen_resolution}")
    print(f"Pencere boyutu: {windowSize}")
    print(f"Ölçekleme: {wincap.scaling*100}%")

    aspect_ratio = windowSize[0]/windowSize[1]
    if aspect_ratio > 1.79:
        print(bcolors.WARNING + "Botun amaçlandığı gibi çalışması için lütfen bluestack'ta reklamları devre dışı bıraktığınızdan ve sağ kenar çubuğunu kapattığınızdan emin olun." + bcolors.ENDC)

    while True:
        screenshot = wincap.screenshot
        if screenshot is None:
            continue
        # update screenshot for dectector
        detector.update(screenshot)
        screendetect.update_bot_stop(bot.stopped)
        # check bot state
        if bot.state == BotState.INITIALIZING:
            bot.update_results(detector.results)
        elif bot.state == BotState.SEARCHING:
            bot.update_results(detector.results)
        elif bot.state == BotState.MOVING:
            bot.update_screenshot(screenshot)
            bot.update_results(detector.results)
        elif bot.state == BotState.HIDING:
            bot.update_results(detector.results)
            bot.update_player(add_two_tuple(detector.player_topleft,wincap.offsets)
                              ,add_two_tuple(detector.player_bottomright,wincap.offsets))
        elif bot.state == BotState.ATTACKING:
            bot.update_results(detector.results)

        # check screendetect state
        if (screendetect.state ==  Detectstate.EXIT
            or screendetect.state ==  Detectstate.PLAY_AGAIN
            or screendetect.state ==  Detectstate.CONNECTION
            or screendetect.state ==  Detectstate.PLAY
            or screendetect.state == Detectstate.PROCEED):
            py.mouseUp(button = Constants.movement_key)
            bot.stop()
        elif screendetect.state ==  Detectstate.LOAD:
            if bot.stopped:
                #wait for game to load
                sleep(4)
                print("Bot Başlatılıyor")
                # reset timestamp and state
                bot.timestamp = time()
                bot.state = BotState.INITIALIZING
                bot.start()

        # display annotated window with FPS
        if Constants.DEBUG:
            detector.annotate_detection_midpoint()
            detector.annotate_border(bot.border_size,bot.tile_w,bot.tile_h)
            detector.annotate_fps(wincap.avg_fps)
            cv.imshow("Brawl Stars Bot",detector.screenshot)

        # Press q to exit the script
        key = cv.waitKey(1)
        x_mouse, y_mouse = py.position()
        if wincap.screen_resolution[1] == (windowSize[1]+wincap.titlebar_pixels+1):
            stop_bool = x_mouse > (wincap.offset_x + wincap.w)
        else:
            stop_bool = ((x_mouse > 0 and x_mouse < wincap.left and y_mouse > 0 and y_mouse < wincap.top)
            or ( x_mouse > wincap.right and x_mouse < wincap.screen_resolution[0]
                and y_mouse > wincap.bottom and y_mouse < wincap.screen_resolution[1]))
        
        if (key == ord('q') or stop_bool):
            #stop all threads
            stop_all_thread(wincap,screendetect,bot,detector)
            break
    print(bcolors.WARNING +'İmleç şu anda Bluestacksta değil, bottan çıkılıyor...' +bcolors.ENDC)
    stop_all_thread(wincap,screendetect,bot,detector)

if __name__ == "__main__":
    print(" ")
    print(bcolors.HEADER + bcolors.BOLD +
              "Botu başlatmadan önce Brawl Starsın açık olduğundan emin olun. \n Solo hesaplaşma oyun modu Seçin.")
    print("")
    print("Ayrıca hızı, attack_range ve HeightScaleFactor'ı değiştirdiğinizden emin olun"
            +"\nconstants.py adresinde seçtiğiniz brawler için (orada da talimat var).")
    print("Bottan çıkmak için imleci sol üst veya sağ alt köşeye getirin.")
    print("")
    print(bcolors.UNDERLINE + "ÖNEMLİ - bluestackta reklamları devre dışı bıraktığınızdan ve sağ kenar çubuğunu kapattığınızdan emin olun" + bcolors.ENDC)
    while True:
        print("")
        print("1. Botu Başlat")
        print("2. Kapatma zamanlayıcısını ayarla")
        print("3. Kapatma zamanlayıcısını iptal et")
        print("4. Çıkış")
        user_input = input("Seçim: ").lower()
        print("")
        # run the bot
        if user_input == "1" or user_input == "start bot":
            main()
        # use cmd to start a shutdown timer
        elif user_input == "2" or user_input == "set shutdown timer":
            print("Kapatma Zamanlayıcısını Ayarla")
            try:
                hour = int(input("Kapanmadan kaç saat önce? "))
                second = 3600 * hour
                os.system(f'cmd /c "shutdown -s -t {second}"')
                print(f" {hour} saat içinde kapanacak")
            except ValueError:
                print("Lütfen geçerli bir girdi girin!")
        # use cmd to cancel shutdown timer
        elif user_input == "3" or user_input == "kapatma zamanlayıcısını iptal et":
            os.system('cmd /c "shutdown -a"')
            print("Zamanlayıcı İptal edildi")
        # exit
        elif user_input =="4" or user_input == "exit":
            print("Çıkılıyor...")
            break