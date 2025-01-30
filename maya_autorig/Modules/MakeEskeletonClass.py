
from maya import cmds

class SkeletonBuilder:
    def __init__(self):
        self.joint_list = []

    def build_skeleton(self, name):
        """
        Example method that creates a single joint with a given name,
        just to illustrate a skeleton-building concept.
        """
        joint_name = cmds.joint(n=name, p=(0,0,0))
        self.joint_list.append(joint_name)
        print(f"Created joint: {joint_name}")
        return joint_name