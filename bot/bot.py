import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from core.engine import BotEngine


def main():
    print("=" * 45)
    print("          LORDSBOT CORE")
    print("=" * 45)

    engine = BotEngine()

    print("Bot motoru hazır.")
    print("Durum:", engine.status.value)
    print("Görev motoru: hazır")
    print("Modül sistemi: hazır")
    print("Kurtarma sistemi: hazır")
    print()

    try:
        while True:
            command = input("LordsBot > ").strip().lower()

            if command == "start":
                if engine.start():
                    print("✓ Bot başlatıldı.")
                else:
                    print("Bot zaten çalışıyor.")

            elif command == "stop":
                if engine.stop():
                    print("✓ Bot durduruldu.")
                else:
                    print("Bot zaten durmuş.")

            elif command == "status":
                print("Durum:", engine.status.value)

            elif command == "exit":
                engine.stop()
                print("LordsBot kapatıldı.")
                break

            else:
                print("Komutlar: start, stop, status, exit")

    except KeyboardInterrupt:
        engine.stop()
        print()
        print("LordsBot güvenli şekilde durduruldu.")


if __name__ == "__main__":
    main()