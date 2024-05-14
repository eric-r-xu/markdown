class CallbackRegistration:
    def __init__(self):
        self.signal_dict = dict()

    def register_callback(self, key, callback):
        if not callable(callback):
            callback = self.create_callback(callback)
        if key not in self.signal_dict:
            self.signal_dict[key] = set()
        self.signal_dict[key].add(callback)
        print(f"Registered callback {callback.__name__} for key {key}")

    def unregister_callback(self, key, callback):
        if key in self.signal_dict:
            for cb in self.signal_dict[key]:
                if cb.__name__ == callback:
                    self.signal_dict[key].remove(cb)
                    print(f"Unregistered callback {callback} for key {key}")
                    return
            print(f"Callback {callback} not found for key {key}")
        else:
            print(f"Callback {callback} not found for key {key}")

    def signal(self, key):
        if key in self.signal_dict:
            for callback in self.signal_dict[key]:
                print(f'Calling {callback.__name__}')
                callback()
        else:
            print(f"No callbacks registered for key {key}")

    def __call__(self, key):
        print(self.signal(key))
        self.signal(key)

    # doesn't depend on self
    @staticmethod
    def create_callback(name):
        def callback():
            print(f"Callback {name} executed")
            print(name)
        callback.__name__ = name
        return callback

# Module-level instance
_cb = CallbackRegistration()

# Module-level functions
def register_callback(key, callback):
    _cb.register_callback(key, callback)

def unregister_callback(key, callback):
    _cb.unregister_callback(key, callback)

def signal(key):
    _cb.signal(key)


# Define variables a, b, c as equaling the string version of their name
for letter in ['a','b','c']:
    exec(f"{letter}='{letter}'")


# Register callbacks by name (will be created dynamically)
register_callback(1, a)
register_callback(1, b)
register_callback(1, c)

# Unregister a callback by name
unregister_callback(1, a)

# Signal the callbacks for key 1
signal(1)


