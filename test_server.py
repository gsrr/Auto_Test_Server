import sys
import server

def test_restart_ha():
    server.restart_ha()

def main():
    func = getattr(sys.modules[__name__], sys.argv[1])
    func()

if __name__ == "__main__":
    main()
