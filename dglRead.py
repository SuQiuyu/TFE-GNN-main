import dgl
import matplotlib.pyplot as plt
import networkx as nx


def visualize_dgl_graph(file_path):
    # 从文件中加载图数据
    graphs, labels = dgl.load_graphs(file_path)
    # 假设文件中只存储了一个图
    graph = graphs[0]


    # 将 DGL 图转换为 NetworkX 图，方便可视化
    nx_graph = graph.to_networkx()


    # 绘制 NetworkX 图
    pos = nx.spring_layout(nx_graph)  # 可以使用不同的布局，如 nx.circular_layout 等
    nx.draw(nx_graph, pos, with_labels=True, node_color=[[.7,.7,.7]], node_size=500)
    plt.title("DGL Graph Visualization")
    plt.show()


if __name__ == "__main__":
    # 请将这里的路径修改为你实际的 dgl 文件的路径
    file_path1 = 'D:/data/pcap2graph/dgl/test_graph.dgl'
    file_path2 = 'D:/data/pcap2graph/dgl/train_graph.dgl'
    file_path3 = 'D:/data/pcap2graph/dgl/header_test_graph.dgl'
    file_path4 = 'D:/data/pcap2graph/dgl/header_train_graph.dgl'
    visualize_dgl_graph(file_path1)