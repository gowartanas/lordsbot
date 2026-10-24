from controller.game_controller import GameController


controller = GameController()

print()
print("=" * 50)
print("LORDSBOT GAME CONTROLLER TEST")
print("=" * 50)

connected = controller.connect()

if connected:

    print()
    print("[TEST] Controller hazır.")
    print("[TEST] Bağlı cihaz:", controller.device)

else:

    print()
    print("[TEST] Henüz Android cihaz/emulator bulunamadı.")

print()