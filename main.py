import networkx as nx
from networkx.algorithms.community import k_clique_communities
import timeit
import RW as sg
import community
import random
import numpy as np

def network_intersection(G, H):
	Gnodes = set(list(G.nodes()))
	Hnodes = set(list(H.nodes()))
	cmnnodes = list(Gnodes & Hnodes)
	Gnew = G.subgraph(cmnnodes)
	Hnew = H.subgraph(cmnnodes)
	newnet = nx.intersection(Gnew, Hnew)
	return newnet

def add_edges_from(G, edgefile):
	efile = open(edgefile, 'r')
	for line in efile:
		split = line.split(' ')
		srcnd = int(split[0])
		endnd = split[1]
		if endnd[-1]=='\n':
			endnd = int(endnd[:-1])
		G.add_edge(srcnd, endnd)
	return G

if __name__ == '__main__':

	G = nx.Graph()

	start = timeit.default_timer()
	G_reply = nx.read_edgelist('./reply.txt', nodetype=int)
	G_mention = nx.read_edgelist('./mention.txt', nodetype=int)
	G_retweet = nx.read_edgelist('./retweet.txt', nodetype=int)
	G_social = nx.read_edgelist('./social1.txt', nodetype=int)
	G_social = add_edges_from(G_social, './social2.txt')

	nodelist = list(G_reply.nodes())

	rand_smpl = [ nodelist[i] for i in sorted(random.sample(range(len(nodelist)), 2000)) ]

	G_reply = G_reply.subgraph(rand_smpl)
	G_mention = G_mention.subgraph(rand_smpl)
	G_retweet = G_retweet.subgraph(rand_smpl)
	G_social = G_social.subgraph(rand_smpl)

	c = list(k_clique_communities(G_social, 4))
	print('c:', len(c))

	mainpart = community.best_partition(G_social)
	print('mainpart:', len(mainpart.values()))

	for commcnt in range(len(c)):
		nodeset = list(c[commcnt])
		Gr = G_reply.subgraph(nodeset)
		Gm = G_mention.subgraph(nodeset)
		Grr = G_retweet.subgraph(nodeset)
		Gs = G_social.subgraph(nodeset)
		#if (nx.is_connected(Gr) and nx.is_connected(Gm) and nx.is_connected(Grr) and nx.is_connected(Gs)):
		#	pass
		#else:
		#	print ('Runtime error, one of the graphs is not connected')
		#	continue
		Garr = [Gr, Gm, Grr, Gs]
		Klist = sg.multiview_IRWK(Garr)
		for K in Klist:
			print('K:',K)
			print('average similarity is:', K.mean())


	stop = timeit.default_timer()
	print('time:', stop-start)