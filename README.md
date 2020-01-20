# AutoTune [unstable.ver-1]

AutoTune is a Machine Learning tool that is useful in designing machine learning models using a few lines of python code, and with it, create, train, and evaluate machine learning pipelines. 


**NOTE:**
    This *README* can be subjected to change at anytime. So don't be suprise if you come back tomorrow and you find that the documentation for this applciation has changed COMPLETELY

## Principles

To guide me (and hopefully other contributors ;)) in knowing why I am building the application in the first place.

1. **Flexibility** <br />
    The tool should allow [advanced] users to make quick changes to their created pipeline. 
    
    So doing things like changing the models used in a pipeline. Adding imputation techniques (few of which are pre-added). Modifying how to deal with imbalanced data

2. **Extensibility** <br />
    Making it easy to add more features and models that don't yet exist. It should also make it possible to add `pytorch` and `tensorflow` created models to be used in the pipeline

3. **Seemless Pipelining** <br />
    This goes hand-in-hand with `Less Coding`. You should make it possible to create Maching learning pipelines by making simple code additions/modifications.

    (this may not change, or reflect what is inside. this is just an example)

    ```python
    import ...

    kaggle_pipeline = SupervisedPipeline(task='regression', metrics='accuracy')

    at_model = kaggle_pipeline
                .feed_data('somefile.csv')
                .impute(column='age', method='mean')
                .oversample(by='target')
                .train(model=GaussianNB(...))
                .output()

    test_data = ...
    at_model.predict(test_data)
    ```

4. **Less Coding**
    Well, Duhh?!

5. **AutoML-ing** [well yes but actually no. May be later] <br/>
    Although, it is debatable on the usefulness of having this, this option could be added as a bonus or last resort feature in the application. I could try to make this feature make use of the pipeline. May be

6. [Optional] If I do get to use this in the future more that not, find a way to store the analysis data in such a way that an AutoML approach can be obtain by understanding how humans make decisions through experience (and not calculate every possiblity) 