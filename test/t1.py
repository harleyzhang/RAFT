from types import SimpleNamespace
import raft

args = SimpleNamespace()
args.model = 'raft-kitti'

model = raft.RAFT(args)
