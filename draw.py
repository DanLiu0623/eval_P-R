import matplotlib.pyplot as plt
import eval

rec, prec, ap = eval.eval('val_new.txt', 'result5.txt')

plt.plot(rec, prec, 'r-')
plt.title('ap: ' + str(ap))
plt.xlabel('recall')
plt.ylabel('precision')
plt.savefig('pre_rec_5.jpg')
plt.show()