"""

Adding wrappers that make the other version models
compatible with the type needed for AutoTUNE

------------------------------------------------------
Currently, the models need to implement `fit`, `predict` and `predict_proba`
Thus, this makes it ideal for using models from libraries like
`scikit-learn`... So using models created from `pytorch` or `tensorflow`,
you'd need them to implement the 3 functions

"""