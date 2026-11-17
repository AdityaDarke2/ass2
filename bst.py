class TrainNode:
    def __init__(self, num, name, dest, time):
        self.num = num
        self.name = name
        self.dest = dest
        self.time = time
        self.left = None
        self.right = None


class TrainSchedule:
    def __init__(self):
        self.root = None


    def add_train(self, num, name, dest, time):
        if not self.root:
            self.root = TrainNode(num, name, dest, time)
        else:
            self.insert(self.root, num, name, dest, time)


    def insert(self, curr, num, name, dest, time):
        if num < curr.num:
            if not curr.left:
                curr.left = TrainNode(num, name, dest, time)
            else:
                self.insert(curr.left, num, name, dest, time)
        elif num > curr.num:
            if not curr.right:
                curr.right = TrainNode(num, name, dest, time)
            else:
                self.insert(curr.right, num, name, dest, time)


    def display(self):
        print("Train No. | Train Name | Destination | Departure")
        print("-" * 50)
        self.inorder(self.root)
        print()


    def inorder(self, curr):
        if curr:
            self.inorder(curr.left)
            print(f"{curr.num} | {curr.name} | {curr.dest} | {curr.time}")
            self.inorder(curr.right)


    def search(self, num):
        res = self.find(self.root, num)
        if res:
            print(f"Found: [{res.num}] {res.name} -> {res.dest} at {res.time}")
        else:
            print(f"Train {num} not found in schedule.")


    def find(self, curr, num):
        if not curr or curr.num == num:
            return curr
        if num < curr.num:
            return self.find(curr.left, num)
        return self.find(curr.right, num)


    def delete(self, num):
        self.root = self.remove(self.root, num)
        print(f"\nRemoved train {num}. Updated schedule:")
        self.display()


    def remove(self, root, num):
        if not root:
            return root


        if num < root.num:
            root.left = self.remove(root.left, num)
        elif num > root.num:
            root.right = self.remove(root.right, num)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left


            temp = self.get_min(root.right)
            root.num = temp.num
            root.name = temp.name
            root.dest = temp.dest
            root.time = temp.time
            root.right = self.remove(root.right, temp.num)


        return root


    def get_min(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr




if __name__ == "__main__":
    sched = TrainSchedule()


    sched.add_train(105, "Deccan Express", "Pune", "06:30")
    sched.add_train(103, "Intercity Express", "Mumbai", "07:15")
    sched.add_train(108, "Shatabdi Express", "Nagpur", "08:00")
    sched.add_train(101, "Duronto Express", "Delhi", "05:45")
    sched.add_train(104, "Vande Bharat", "Nashik", "09:30")
    sched.add_train(107, "Rajdhani Express", "Delhi", "16:00")
    sched.add_train(110, "Garib Rath", "Goa", "18:30")


    sched.display()


    sched.search(104)
    sched.search(115)


    sched.delete(103)
