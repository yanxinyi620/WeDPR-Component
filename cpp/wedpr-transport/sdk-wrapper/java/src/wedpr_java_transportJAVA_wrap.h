/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (https://www.swig.org).
 * Version 4.2.1
 *
 * Do not make changes to this file unless you know what you are doing - modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

#ifndef SWIG_wedpr_java_transport_WRAP_H_
#define SWIG_wedpr_java_transport_WRAP_H_

class SwigDirector_ErrorCallback : public ppc::front::ErrorCallback, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_ErrorCallback(JNIEnv *jenv);
    virtual ~SwigDirector_ErrorCallback();
    virtual void onError(bcos::Error::Ptr error);
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    Swig::BoolArray<1> swig_override;
};

class SwigDirector_MessageDispatcherHandler : public ppc::front::MessageDispatcherHandler, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_MessageDispatcherHandler(JNIEnv *jenv);
    virtual ~SwigDirector_MessageDispatcherHandler();
    virtual void onMessage(ppc::protocol::Message::Ptr msg);
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    Swig::BoolArray<1> swig_override;
};

class SwigDirector_IMessageHandler : public ppc::front::IMessageHandler, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_IMessageHandler(JNIEnv *jenv);
    virtual ~SwigDirector_IMessageHandler();
    virtual void onMessage(bcos::Error::Ptr e,ppc::protocol::Message::Ptr msg,ppc::front::SendResponseHandler sendResponseHandler);
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    Swig::BoolArray<1> swig_override;
};

class SwigDirector_GetPeersInfoHandler : public ppc::front::GetPeersInfoHandler, public Swig::Director {

public:
    void swig_connect_director(JNIEnv *jenv, jobject jself, jclass jcls, bool swig_mem_own, bool weak_global);
    SwigDirector_GetPeersInfoHandler(JNIEnv *jenv);
    virtual ~SwigDirector_GetPeersInfoHandler();
    virtual void onPeersInfo(bcos::Error::Ptr e,std::string const &peersInfo);
public:
    bool swig_overrides(int n) {
      return (n < 1 ? swig_override[n] : false);
    }
protected:
    Swig::BoolArray<1> swig_override;
};


#endif
